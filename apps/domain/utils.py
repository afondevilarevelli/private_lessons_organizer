import json

def get_htmx_flash_message_header(message: str, tag = "info"):
    return {
        'HX-Trigger': json.dumps(
            {'toast-message': {
                'message': message,
                "tag": tag
            }}
        )
    }