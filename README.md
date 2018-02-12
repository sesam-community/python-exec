# python exec microservice

Pass the code to execute as environment variable "EXEC".

Environment variables are printed by default.

Flask is available.

## Example usage

    {
      "_id": "debugger",
      "type": "system:microservice",
      "docker": {
        "environment": {
          "secrets": {
            "FOO": "$SECRET(FOO)"
          }
        },
        "image": "sesamcommunity/python-exec",
        "port": 5001
      }
    }

Default output (prints environment variables):

    2018-02-12T11:27:48.107993562Z secrets: {"FOO": "bar"}
