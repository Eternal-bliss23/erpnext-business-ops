#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
env_file="${root_dir}/.env.business"

if ! command -v docker >/dev/null 2>&1 || ! docker compose version >/dev/null 2>&1; then
  echo "Docker Engine with Docker Compose v2 is required. Install it, then rerun this command." >&2
  exit 1
fi

if [[ ! -f "${env_file}" ]]; then
  echo "Missing ${env_file}. Copy .env.business.example and set secure passwords." >&2
  exit 1
fi

# shellcheck disable=SC1090
source "${env_file}"

docker build \
  --build-arg "ERPNEXT_VERSION=${ERPNEXT_VERSION}" \
  --tag "${CUSTOM_IMAGE}:${CUSTOM_TAG}" \
  --file "${root_dir}/Dockerfile.business" \
  "${root_dir}"

"${root_dir}/scripts/render-compose.sh"
docker compose --env-file "${env_file}" -f "${root_dir}/compose.generated.yaml" -p business-erp up -d

echo "Waiting for the database and Frappe configurator to be ready..."
sleep 15

# Site creation is safe to re-run: it only creates the site when it is absent.
if ! docker compose --env-file "${env_file}" -f "${root_dir}/compose.generated.yaml" -p business-erp \
  exec -T backend test -d "sites/${SITE_NAME}"; then
  docker compose --env-file "${env_file}" -f "${root_dir}/compose.generated.yaml" -p business-erp \
    exec -T backend bench new-site "${SITE_NAME}" \
      --mariadb-user-host-login-scope='172.%.%.%' \
      --db-root-password "${DB_PASSWORD}" \
      --admin-password "${ADMIN_PASSWORD}" \
      --install-app erpnext \
      --install-app business_ops
fi

echo "ERP is ready at http://localhost:${HTTP_PUBLISH_PORT}"
