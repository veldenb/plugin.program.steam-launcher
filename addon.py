import xbmcaddon
import xbmcgui
from subprocess import PIPE, run

# # Configure addon
addon = xbmcaddon.Addon()
executable = addon.getSettingString('command_to_execute')

if executable:
    result = run([executable], stdout=PIPE, stderr=PIPE, universal_newlines=True)

    # Check if command was successful
    if result.returncode != 0:
        dialog = xbmcgui.Dialog()
        dialog.ok(addon.getLocalizedString(30004), result.stdout + result.stderr)
else:
    addon.openSettings()
