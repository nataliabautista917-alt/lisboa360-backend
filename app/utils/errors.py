"""Manejo centralizado de errores — respuestas JSON estandarizadas según el contrato OpenAPI."""
from flask import jsonify


class AppError(Exception):
    """Excepción base para errores de aplicación con respuesta estandarizada."""

    def __init__(self, code: str, message: str, status_code: int, details=None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details if details is not None else {}


class ValidationError(AppError):
    """Error de validación (código 422, según contrato OpenAPI)."""

    def __init__(self, message: str, details=None):
        super().__init__("VALIDATION_ERROR", message, 422, details)


class NotFoundError(AppError):
    """Recurso no encontrado (código 404)."""

    def __init__(self, message: str):
        super().__init__("NOT_FOUND", message, 404)


class InternalError(AppError):
    """Error interno del servidor (código 500)."""

    def __init__(self, message: str):
        super().__init__("INTERNAL_ERROR", message, 500)


def _error_payload(code, message, details=None):
    return {
        "error": {
            "code": code,
            "message": message,
            "details": details if details is not None else {},
        }
    }


def register_error_handlers(app):
    """Registra manejadores de errores que devuelven respuestas JSON estandarizadas."""

    @app.errorhandler(AppError)
    def handle_app_error(error):
        return jsonify(_error_payload(error.code, error.message, error.details)), error.status_code

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify(_error_payload(error.code, error.message, error.details)), error.status_code

    @app.errorhandler(NotFoundError)
    def handle_not_found_error(error):
        return jsonify(_error_payload(error.code, error.message, error.details)), error.status_code

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        app.logger.exception("Error interno no controlado")
        return jsonify(_error_payload("INTERNAL_ERROR", "Error interno del servidor.", {})), 500

    @app.errorhandler(404)
    def handle_http_not_found(error):
        return jsonify(_error_payload("NOT_FOUND", "Recurso no encontrado.")), 404

    @app.errorhandler(405)
    def handle_http_method_not_allowed(error):
        return jsonify(_error_payload("METHOD_NOT_ALLOWED", "Método no permitido.")), 405

    @app.errorhandler(400)
    def handle_http_bad_request(error):
        return jsonify(_error_payload("VALIDATION_ERROR", "Solicitud inválida.")), 400
