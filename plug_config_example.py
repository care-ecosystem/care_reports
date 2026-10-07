from plugs.plug import Plug

care_reports_plugin = Plug(
    name="care_reports",
    package_name="/app/care_reports",       # local dev path; use git+https://... in production
    version="",                               # keep empty for local dev; "@main" for production
    configs={
        # TODO: add your plugin settings here
        # "MYPLUGIN_API_KEY": "your-api-key",
    },
)

# In plug_config.py, add to plugs list:
# plugs = [
#     care_reports_plugin,
# ]
