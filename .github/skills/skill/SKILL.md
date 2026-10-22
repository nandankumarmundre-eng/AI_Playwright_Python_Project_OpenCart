---
name: skill
description: Playwright Python Pytest Page Object Model expert skill for creating maintainable, type-safe automation using POM architecture.
---

# Skills: Playwright Python Pytest Page Object Model (POM)

**Skill Name**: Playwright POM Expert
**Version**: 1.0
**Language**: Python (Strict)
**Framework**: Playwright Test Runner

## Core Expertise

### 1. Playwright Framework Mastery
- Full command of 'playwright/tests'
- Advanced locator strategies and auto-waiting mechanisms
- Network, DOM, and Load state handling
- Tracing, screenshots, video recording on failure
- API testing using 'request' fixture
- Authentication flows ('storageState', auth fixtures)
- Device emulation and mobile testing

## 2. Page Object Model Architecture
- Strict Page Object Model implementation
- BasePage and BaseComponent pattern
- Composition over inheritance (Pages containing Components)
- Fluent API design ('return this')
- Seperation of concerns: Locators, Actions, Assertions
- Reusable component library creation
- Type-safe page objects

## 3. Python Advanced Usage
- Strict Python configuration
- Readonly locators and properties
- Generic test fixtures using 'test.extend()
- Interface and type definitions
- Proper sync patterns
- Error handling and custom assertions
- Pytest framework - module names starts with(test_)
- test functions start with (test_)

## 4. Locator Strategy (Priority Order)
1. **'get_by_test_id()'** - Preferred (data-testid)
2. **'get_by_role()'** - With accessible name
3. **'get_by_label()'**
4. **'get_by_placeholder()'**
5. **'get_by_alt_text()'**
6. **'get_by_text()'**  - Only when necessary
7. CSS selectors - Last resort with justification
8. frame_locator() - for iframes

## 5. Prohibited Practices
- Inline locators in methods
- XPath locators
- Hard-coded timeouts
- Using 'Page.locator()' directly in tests
- Mixing assertions inside page objects
- Non-accessible locators without reason

## Deliverables
I  can create and maintain:
- Complete Page Objects
- Reusable UI Components
- Base classes ('BasePage', 'BaseComponent')
- Custom fixtures
- Optimized 'Playwright.config.py'
- Utility functions
- Authentication flows
- Full test specifications
- pytest.ini
- conftest.py

## Quality Standards

All code I produce will meet these standards:
- 100% type safety
- Locators declared at class level
- Clear, descriptive method names
- Small, focused methods
- Fluent compatibility with CI/CD
- Accessibility-first approach

---
