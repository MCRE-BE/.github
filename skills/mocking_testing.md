# Mocking & Testing Diagnostics

- **Mocking External APIs:** Use `unittest.mock` (such as `unittest.mock.MagicMock` or `monkeypatch` in pytest) to mock external network requests, database connections, or file systems.
- **Mock Verification:** Always assert that mocks were called with the correct parameters (e.g. `mock_method.assert_called_once_with(...)`).
