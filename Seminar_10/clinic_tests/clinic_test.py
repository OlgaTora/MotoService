from unittest import mock
import pytest
from starlette.testclient import TestClient

from Arcitecture.Seminar_10.clinic.repositories.clients_repository import ClientRepository
from Arcitecture.Seminar_10.clinic.schemas.client import Client
from Arcitecture.Seminar_10.clinic.services.app import app
from Arcitecture.Seminar_10.clinic.services.clients import ClientService
from Arcitecture.Seminar_10.clinic.services.depends import get_client_service


@pytest.fixture
def client():
    client = TestClient(app)
    yield client


def test_get_all_clients(client):
    # [1] Подготовка данных для тестирования
    # Создаем мок-объект для зависимости
    client_repo_mock = mock.AsyncMock(spec=ClientRepository)
    client_repo_mock.get_all.return_value = [
        Client(client_id=1, document="123", surname='test1', firstname='test1', patronymic='test1',
               birthday='2012-01-10'),
        Client(client_id=2, document="131", surname='test2', firstname='test2', patronymic='test2',
               birthday='2012-11-10'),
    ]

    # [2] Исполнение тестируемого метода
    # Создаем объект, который мы будем тестировать

    def get_client_service_override() -> ClientService:
        return client_repo_mock

    app.dependency_overrides[get_client_service] = get_client_service_override

    # [3] Подготовка эталонного результата, проверка результата
    response = client.get('/get-all-clients/')
    assert response.status_code == 200
    data = response.json()
    assert data == [
        {'client_id': 1, 'document': "123", 'surname': 'test1', 'firstname': 'test1', 'patronymic': 'test1',
         'birthday': '2012-01-10'},
        {'client_id': 2, 'document': "131", 'surname': 'test2', 'firstname': 'test2', 'patronymic': 'test2',
         'birthday': '2012-11-10'},
    ]


def test_create_client(client):
    # [1] Подготовка данных для тестирования
    # Создаем мок-объект для зависимости
    client_repo_mock = mock.AsyncMock(spec=ClientRepository)
    client_repo_mock.create.return_value = {'client_id': 3, 'document': "231", 'surname': 'test3', 'firstname': 'test3',
                                            'patronymic': 'test3',
                                            'birthday': '2012-11-10'}

    # [2] Исполнение тестируемого метода
    # Создаем объект, который мы будем тестировать
    def get_client_service_override() -> ClientService:
        return client_repo_mock

    app.dependency_overrides[get_client_service] = get_client_service_override
    # [3] Подготовка эталонного результата, проверка результата
    client_create = {'document': "231", 'surname': 'test3', 'firstname': 'test3',
                     'patronymic': 'test3',
                     'birthday': '2012-11-10'}
    response = client.post('/create-new-client/', json=client_create)
    assert response.status_code == 200
    data = response.json()
    assert data == client_repo_mock.create.return_value

    if __name__ == '__main__':
        pytest.main(['-v'])
