# Deployment Information

> **Lưu ý:** Điền URL public và chụp 3 ảnh lưu vào thư mục `screenshots/` sau khi deploy thư mục `06-lab-complete/` lên Railway hoặc Render.

## Public URL

`https://lab14-production-39329102.up.railway.app/`

## Platform

`Railway`


## Test Commands

```bash
BASE="https://lab14-production-39329102.up.railway.app/"
AGENT_API_KEY="Open_Code"

# 1. Health check (kỳ vọng: 200)
curl -sS -o /dev/null -w '%{http_code}\n' "$BASE/health"

# 2. Readiness check (kỳ vọng: 200)
curl -sS -o /dev/null -w '%{http_code}\n' "$BASE/ready"

# 3. Ask không có API key (kỳ vọng: 401)
curl -sS -o /dev/null -w '%{http_code}\n' -X POST "$BASE/ask" \
  -H 'Content-Type: application/json' \
  -d '{"question":"Hello"}'

# 4. Ask có API key (kỳ vọng: 200)
curl -sS -o /dev/null -w '%{http_code}\n' -X POST "$BASE/ask" \
  -H 'Content-Type: application/json' \
  -H "X-API-Key: $AGENT_API_KEY" \
  -d '{"question":"Hello"}'
```

## Environment Variables Set

- `PORT` (do nền tảng tự inject hoặc đặt `8000`)
- `REDIS_URL` (kết nối tới Redis add-on trên nền tảng)
- `AGENT_API_KEY` (đặt trên Dashboard/CLI, **không** commit vào code)
- `ENVIRONMENT=production`
- `LOG_LEVEL=INFO`

## Screenshots (Cần bổ sung sau khi deploy)

- [x] [Deployment dashboard](screenshots/dashboard.png) — *Chụp giao diện Railway/Render thấy service + biến môi trường (che secret)*
- [x] [Service running](screenshots/running.png) — *Chụp trạng thái service Active/Live và logs khởi động*
- [x] [Test results](screenshots/test.png) — *Chụp terminal chạy 4 lệnh `curl` tự kiểm tra ở trên (ra `200`, `200`, `401`, `200`)*
