def message(status, message):
    return {
        "status": status,
        "message": message
    }


def validation_error(status,errors):
    response_object = {"status": status, "errors": errors}
    return response_object


def err_resp(msg, reason, code):
    err = message(False, msg)
    err["error_reason"] = reason
    return err, code


def internal_err_resp():
    err = message(False,"Internal Server Error")
    err["errors_reason"] = "server_error"
    return err,500