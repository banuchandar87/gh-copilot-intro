# Plan: FastAPI Backend Tests (AAA Pattern)

We will add backend tests for the FastAPI app using the Arrange-Act-Assert (AAA) pattern for clarity and maintainability.

**Steps**
1. Create a `tests/` directory at the project root for all backend test files.
2. Add an initial test file, e.g., `tests/test_app.py`.
3. In each test, use the AAA pattern:
   - **Arrange:** Set up the test environment, data, and FastAPI TestClient.
   - **Act:** Make the API call (GET/POST) to the endpoint under test.
   - **Assert:** Check the response status, data, and any side effects.
4. Write tests for key endpoints:
   - `/activities` (GET): Returns all activities.
   - `/activities/{activity_name}/signup` (POST): Register a participant, handle already registered, and not found.
   - `/activities/{activity_name}/unregister` (POST): Unregister a participant, handle not registered, and not found.
5. Use fixtures to reset in-memory data between tests if needed.
6. Run tests with `pytest` to verify backend functionality.
7. Expand coverage for new endpoints or edge cases as needed.

**Relevant files**
- `src/app.py` — FastAPI app and endpoints
- `tests/test_app.py` — New test file for backend API
- `pytest.ini` — Pytest config

**Verification**
1. Run `pytest` and ensure all tests pass.
2. Confirm tests follow the AAA pattern for readability.

**Decisions**
- All tests will be structured using the AAA pattern for consistency.
- Tests will be placed in a new `tests/` directory at the project root.
- In-memory data will be reset between tests to avoid cross-test contamination.
