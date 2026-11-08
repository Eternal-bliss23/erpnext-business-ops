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

docker compose --env-file "${env_file}" \
  -f "${root_dir}/compose.yaml" \
  -f "${root_dir}/overrides/compose.mariadb.yaml" \
  -f "${root_dir}/overrides/compose.redis.yaml" \
  -f "${root_dir}/overrides/compose.noproxy.yaml" \
  -f "${root_dir}/compose.business.yaml" \
  config > "${root_dir}/compose.generated.yaml"

echo "Wrote ${root_dir}/compose.generated.yaml"
