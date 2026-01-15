# Pytest 테스트 가이드

## 테스트 실행

### 모든 테스트 실행
```bash
pytest
```

### 특정 마커만 실행
```bash
pytest -m unit           # 단위 테스트만
pytest -m api            # API 테스트만
pytest -m integration    # 통합 테스트만
pytest -m "not slow"     # 느린 테스트 제외
```

### 특정 파일/디렉토리 실행
```bash
pytest tests/unit/                    # unit 테스트만
pytest tests/api/test_home_routes.py  # 특정 파일
pytest tests/unit/test_config.py::test_config_default_values  # 특정 테스트
```

### 커버리지 리포트
```bash
pytest --cov=backend --cov-report=html
# htmlcov/index.html 파일 열어서 확인
```

## 테스트 작성 가이드

### 1. 단위 테스트 (Unit Tests)
- 개별 함수/클래스의 로직 테스트
- 외부 의존성 없이 독립적으로 실행
- `tests/unit/` 디렉토리

### 2. 통합 테스트 (Integration Tests)
- 여러 컴포넌트 간 상호작용 테스트
- DB, 외부 서비스 등 실제 연동
- `tests/integration/` 디렉토리

### 3. API 테스트 (API Tests)
- FastAPI 엔드포인트 테스트
- TestClient 사용
- `tests/api/` 디렉토리

## Fixture 사용

```python
def test_with_client(client):
    """client fixture 사용"""
    response = client.get("/")
    assert response.status_code == 200

def test_with_mock(mocker):
    """pytest-mock 사용"""
    mock_func = mocker.patch('module.function')
    mock_func.return_value = "mocked"
```

## 비동기 테스트

```python
@pytest.mark.asyncio
async def test_async_function():
    result = await some_async_function()
    assert result == expected
```

## 주의사항

- 실제 증권사 API 호출은 `@pytest.mark.skip` 사용
- DB 테스트는 임시 DB 또는 트랜잭션 롤백 활용
- 민감한 정보(API 키 등)는 환경변수나 mock 사용
