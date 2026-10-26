# Bug: System accepts duplicate ISBNs

**Description:** The system allows the same ISBN to be registered more than once.

**Steps to Reproduce:**
1. Log in as a librarian.
2. Register a book with ISBN `9781234567890`.
3. Register another book using the same ISBN.

**Expected Result:** The system should reject the duplicate ISBN.

**Actual Result:** The system registers the same ISBN twice.

**Severity:** High

**Priority:** High