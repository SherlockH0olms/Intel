# Contributing to Intellica

Töhfələrinizi qəbul edirik! Bu qaydalar layihəyə necə töhfə verəcəyinizi izah edir.

## Development Workflow

1. Repository-ni fork edin
2. Feature branch yaradın: `git checkout -b feature/yeni-xusussiyyet`
3. Dəyişiklikləri commit edin: `git commit -m 'feat: yeni xüsusiyyət əlavə et'`
4. Branch-ı push edin: `git push origin feature/yeni-xusussiyyet`
5. Pull Request açın

## Commit Message Format

```
<type>: <subject>

<body>
```

**Types:**
- `feat`: Yeni xüsusiyyət
- `fix`: Bug düzəlişi
- `docs`: Dokumentasiya
- `style`: Formatlaşdırma
- `refactor`: Kod refaktorinqi
- `test`: Test əlavəsi
- `chore`: Build və ya tool dəyişiklikləri

## Code Style

- **Python**: PEP 8, Black formatter
- **TypeScript**: ESLint + Prettier
- **Commit**: Conventional Commits

## Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## Pull Request Guidelines

- PR-ınızı açmazdan əvvəl test etdiyinizə əmin olun
- Açıq və dətaylı izahat yazın
- Kodunuzu dokumentasiya ilə təmin edin
- Bir PR-da tək bir feature əlavə edin

## Development Setup

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pytest black pylint
```

### Frontend
```bash
cd frontend
npm install
npm run lint
```

## Questions?

GitHub Issues-də sual verin və ya discussion açın.

## Code of Conduct

Layihədə iştirak edərkən hörmətli və konstruktiv olun. Töhfə verənlər arasında heç bir ayrd-seçmə edilməməlidir.

---

Təşəkkürlər! 🚀