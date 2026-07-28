
class WTCApiUnauthorizedError(Exception):
    """Exception raised for unauthorized access"""

class WTCApiDisabledError(Exception):
    """Exception raised when accessing the disabled API"""

class WTCApiTemporaryError(Exception):
    """Exception raised when a temporary api failure occurs"""