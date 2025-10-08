# Contributing to BlueHat Security

Thank you for your interest in contributing to BlueHat Security! This document provides guidelines and information for contributors.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

## Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inclusive environment for all contributors.

### Expected Behavior
- Be respectful and constructive
- Focus on what is best for the community
- Show empathy towards others
- Accept constructive criticism gracefully

### Unacceptable Behavior
- Harassment or discrimination of any kind
- Trolling, insulting, or derogatory comments
- Publishing others' private information
- Any conduct inappropriate in a professional setting

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/BlueHat-Security.git
   cd BlueHat-Security
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** following our coding standards
5. **Test your changes** thoroughly
6. **Submit a pull request**

## How to Contribute

### Types of Contributions

#### Bug Fixes
- Fix identified bugs
- Improve error handling
- Resolve edge cases

#### New Features
- Add new security monitoring capabilities
- Enhance existing features
- Improve user interface

#### Documentation
- Improve README and guides
- Add code comments
- Create tutorials

#### Testing
- Add test cases
- Improve test coverage
- Report bugs

## Development Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git

### Setup Steps

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests**:
   ```bash
   python test_bluehat.py
   ```

3. **Run the application**:
   ```bash
   python bluehat_security.py
   ```

### Development Environment

Recommended tools:
- **IDE**: Visual Studio Code, PyCharm, or similar
- **Python Linter**: pylint or flake8
- **Code Formatter**: black or autopep8

## Coding Standards

### Python Style Guide
Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide:

- Use 4 spaces for indentation (not tabs)
- Maximum line length: 88 characters (or 79 for strict PEP 8)
- Use meaningful variable names
- Add docstrings to all functions and classes

### Code Structure

```python
def function_name(param1, param2):
    """
    Brief description of function.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
        
    Returns:
        type: Description of return value
    """
    # Implementation
    pass
```

### Naming Conventions
- **Functions**: `lowercase_with_underscores`
- **Classes**: `CamelCase`
- **Constants**: `UPPERCASE_WITH_UNDERSCORES`
- **Private methods**: `_leading_underscore`

### Comments
- Write clear, concise comments
- Explain "why" not "what" when possible
- Update comments when code changes
- Use docstrings for functions and classes

## Testing

### Running Tests
```bash
python test_bluehat.py
```

### Writing Tests

Add tests for new features in `test_bluehat.py`:

```python
def test_new_feature():
    """Test description"""
    # Arrange
    expected = "expected value"
    
    # Act
    result = new_feature()
    
    # Assert
    assert result == expected
    print("✓ Test passed")
    return True
```

### Test Coverage
- Write tests for all new functions
- Test edge cases and error conditions
- Ensure existing tests still pass
- Aim for high code coverage

## Pull Request Process

### Before Submitting

1. **Update documentation** if needed
2. **Run all tests** and ensure they pass
3. **Check code style** with a linter
4. **Test on Windows 11** if possible
5. **Update CHANGELOG.md** if appropriate

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
Describe testing performed

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] CHANGELOG.md updated (if needed)
```

### Review Process

1. Maintainers will review your PR
2. Address any requested changes
3. Once approved, PR will be merged
4. Your contribution will be credited

## Reporting Bugs

### Before Reporting
- Check existing issues to avoid duplicates
- Test with the latest version
- Gather relevant information

### Bug Report Template

```markdown
**Bug Description**
Clear description of the bug

**Steps to Reproduce**
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: Windows 11
- Python Version: 3.11.0
- BlueHat Version: 1.0.0

**Screenshots**
If applicable

**Additional Context**
Any other relevant information
```

## Suggesting Features

### Feature Request Template

```markdown
**Feature Description**
Clear description of the feature

**Use Case**
Why is this feature needed?

**Proposed Solution**
How should it work?

**Alternatives Considered**
Other solutions you've thought about

**Additional Context**
Any other relevant information
```

## Development Guidelines

### Security Considerations
- Never commit secrets or credentials
- Validate all user input
- Use safe file operations
- Follow principle of least privilege
- Test security implications

### Performance Guidelines
- Avoid blocking the UI thread
- Use threading for long operations
- Optimize loops and iterations
- Monitor resource usage
- Profile performance-critical code

### User Experience
- Keep UI responsive
- Provide clear feedback
- Handle errors gracefully
- Use consistent styling
- Test usability

## Git Workflow

### Commit Messages
Use clear, descriptive commit messages:

```
Add network connection filtering feature

- Implement filter by connection status
- Add UI controls for filtering
- Update documentation
- Add tests for filter functionality
```

### Branch Naming
- `feature/feature-name` - New features
- `bugfix/bug-description` - Bug fixes
- `docs/documentation-update` - Documentation
- `refactor/code-improvement` - Code refactoring

## Questions?

If you have questions:
1. Check existing documentation
2. Search closed issues
3. Open a new issue with your question
4. Tag it with "question" label

## Recognition

Contributors will be:
- Listed in release notes
- Credited in commits
- Acknowledged in documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to BlueHat Security! 🛡️

Together, we can make Windows 11 security monitoring better for everyone.
