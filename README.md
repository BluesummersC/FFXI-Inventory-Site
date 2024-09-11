# FFXI-Inventory-Site
A self-hosted webpage to make it easier to filter and search all of your inventories.

This requires a ton of setup! Mainly, a DB that contains all the FFXI armour/item resources and a plugin that outputs all of your inventories into a flat file that can be cross-checked to the resources!

You must have Windower and the plugin called Organizer. This plugin will output your inventory into a static file.
Load the output from Organizer into a MySQLdb, edit dbconnect.py with the correct info.

If Organizer has been updated or removed, this won't work until a new solution is made.
