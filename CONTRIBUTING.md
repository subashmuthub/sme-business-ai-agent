# Contributing to SME Business AI Agent

We welcome contributions to the SME Business AI Agent project! This document provides guidelines for contributing.

## 🤝 How to Contribute

### Reporting Issues
- Use GitHub Issues to report bugs or request features
- Provide clear description and steps to reproduce
- Include system information (OS, Python version, etc.)

### Pull Requests
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Commit your changes (`git commit -m 'Add your feature'`)
7. Push to your branch (`git push origin feature/your-feature`)
8. Create a Pull Request

## 📋 Development Setup

### Prerequisites
- Python 3.11 or higher
- Git
- Virtual environment tool

### Setup Steps
```bash
# Clone your fork
git clone https://github.com/yourusername/sme-business-ai-agent.git
cd sme-business-ai-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Run tests
pytest

# Format code
black .

# Lint code
flake8 .
```

## 🎯 Areas for Contribution

### 🐛 Bug Fixes
- Fix calculation errors in business metrics
- Improve error handling
- UI/UX improvements

### ✨ New Features
- Additional business metrics
- New visualization types
- Integration with external APIs
- Mobile responsive design

### 📚 Documentation
- API documentation
- User guides
- Video tutorials
- Translation to other languages

### 🧪 Testing
- Unit tests for business logic
- Integration tests for web interfaces
- Performance testing
- User acceptance testing

## 📝 Coding Standards

### Python Style
- Follow PEP 8 guidelines
- Use type hints where possible
- Write docstrings for functions and classes
- Keep functions small and focused

### Code Structure
```python
def calculate_profit_margin(sales: float, expenses: float) -> float:
    """Calculate profit margin as a percentage.
    
    Args:
        sales: Total sales amount
        expenses: Total expenses amount
        
    Returns:
        Profit margin as percentage (0-100)
        
    Raises:
        ValueError: If sales is zero or negative
    """
    if sales <= 0:
        raise ValueError("Sales must be positive")
    
    profit = sales - expenses
    return (profit / sales) * 100
```

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove)
- Keep first line under 50 characters
- Use body for detailed explanation if needed

Examples:
```
Add customer retention rate calculation
Fix quarterly report generation bug
Update dashboard UI for mobile devices
```

## 🧪 Testing Guidelines

### Test Structure
```python
def test_profit_margin_calculation():
    """Test profit margin calculation with valid inputs."""
    sales = 100000
    expenses = 75000
    expected_margin = 25.0
    
    result = calculate_profit_margin(sales, expenses)
    assert result == expected_margin

def test_profit_margin_zero_sales():
    """Test profit margin calculation with zero sales."""
    with pytest.raises(ValueError):
        calculate_profit_margin(0, 1000)
```

### Test Coverage
- Aim for 80%+ test coverage
- Test both positive and negative scenarios
- Include edge cases and error conditions

## 📋 Pull Request Checklist

Before submitting a pull request, ensure:

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] No merge conflicts
- [ ] Clear description of changes
- [ ] Screenshots for UI changes

## 🔍 Code Review Process

1. **Automated Checks**: All PRs run automated tests
2. **Peer Review**: At least one maintainer reviews each PR
3. **Testing**: Changes are tested in development environment
4. **Documentation**: Ensure documentation is updated
5. **Merge**: Approved PRs are merged to main branch

## 🚀 Release Process

### Versioning
We use Semantic Versioning (SemVer):
- **Major**: Breaking changes
- **Minor**: New features, backward compatible
- **Patch**: Bug fixes, backward compatible

### Release Steps
1. Update version numbers
2. Update CHANGELOG.md
3. Create release tag
4. Build and test release
5. Publish to GitHub releases

## 💬 Communication

### Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Requests**: Code contributions and reviews

### Response Times
- We aim to respond to issues within 48 hours
- Pull requests are reviewed within one week
- Critical bugs are prioritized

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors are recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to SME Business AI Agent! 🎉