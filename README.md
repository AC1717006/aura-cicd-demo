# aura-cicd-demo

A tiny CI/CD demo for beginners (Aura Automation, "CI/CD Kya Hai? GitHub Actions Beginners Ke Liye").

- `discount.py` — order above ₹1000 gets a 10% discount (`DISCOUNT_RATE`)
- `test_discount.py` — pytest tests (₹1500 → ₹150, ₹900 → ₹0)
- `site/index.html` — a small "Discount Calculator" page (same rule in JavaScript)
- `.github/workflows/ci.yml` — GitHub Actions workflow

## What the workflow does

On every `push`:

1. **test** job (`ubuntu-latest`): checkout → set up Python → `pip install pytest` → `pytest`
2. **deploy** job (`needs: test`): uploads `site/` and deploys it to GitHub Pages

If a test fails, the deploy job is skipped, so a broken change never goes live.

## Run the tests locally

```
pip install pytest
pytest
```
Git vs GitHub video ke liye update ✅
