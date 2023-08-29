from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    app_description: str = ('Приложение для Благотворительного фонда поддержки котиков')
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None
    AMOUNT_DAYS_FOR_EXAMPLE: Optional[int] = 1
    FROM_TIME: Optional[datetime] = datetime.utcnow().isoformat(timespec='minutes')
    TO_TIME: Optional[datetime] = ((datetime.utcnow() +
                                    timedelta(days=AMOUNT_DAYS_FOR_EXAMPLE)).isoformat(
                                        timespec='minutes'))
    FOR_EXAMPLE: Optional[int] = 1
    MIN_LENGHT: Optional[int] = 1
    MAX_LENGHT: Optional[int] = 100

    class Config:
        env_file = '.env'


settings = Settings()