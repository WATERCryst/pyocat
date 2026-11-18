class WTCApiError(Exception):
    """WATERCryst base exception"""

class WTCApiCancelledError(WTCApiError):
    """Exception raised when an async request is cancelled"""

class WTCApiDisabledError(WTCApiError):
    """Exception raised when accessing the disabled API"""

class WTCApiQuotaExceededError(WTCApiError):
    """Exception raised when the request quota has been exceeded"""

class WTCApiRequestError(WTCApiError):
    """Exception raised when a client-side error occurs"""

class WTCApiServerError(WTCApiError):
    """Exception raised when a server-side API failure occurs"""

class WTCApiTimeoutError(WTCApiError):
    """Exception raised when a request timeout occurs"""

class WTCApiUnauthorizedError(WTCApiError):
    """Exception raised for unauthorized access"""

class WTCApiValidationError(WTCApiError):
    """Exception raised when model validation failed"""
