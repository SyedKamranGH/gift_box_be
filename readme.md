| API Endpoint                 | Method | Auth Required | Role Needed | Description                                |
| ---------------------------- | ------ | ------------- | ----------- | ------------------------------------------ |
| `/api/auth/register/`        | POST   | ❌             | None        | Register with username/email/password/role |
| `/api/auth/login/`           | POST   | ❌             | None        | Login and get JWT tokens                   |
| `/api/auth/profile/`         | GET    | ✅             | Any         | Get current logged-in user info            |
| `/api/auth/change-password/` | POST   | ✅             | Any         | Change password                            |
| `/api/buyer-only/`           | GET    | ✅             | Buyer       | Buyer-only route                           |
