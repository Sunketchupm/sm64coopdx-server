FrozenAlex told me to make this repo.

# Prerequesites:
- [Docker](https://www.docker.com/)
- SM64 ROM file
# Running
Make sure the ROM file is in the same folder as `compose.yaml`.<br>
To run:
```
docker compose up -d
```
To stop:
```
docker compose down
```
To enable server auto-restart (Linux):
```
python3 restart.py &
```
(The script itself is platform agnostic, but other platforms may require a different execution command)
# Configuration
To change server settings, you need to modify `sm64config.txt` (the one located in `config`) Parsing this can be hard, so what you can do instead is change `sm64config_template.txt`. This file has the server settings that matter at the top, as well as the moderator/ban list.<br>
Once you make your changes, you can copy `sm64config_template.txt` into `config` and rename it to `sm64config.txt`.
## Structure
### Server Host
- `coop_player_name` [name]
- `enable-mod:` [mod name]<br>
The file/folder name of the mod to enable (include `.lua` if it's a single file mod, otherwise don't).<br>
Multiple mods can be enabled by adding more `enable-mod:` lines. Mods can be disabled by removing their respective `enable-mod:` line.
### Server Settings
- `coop_player_interaction` [0|1|2]<br>
`0` is Non-solid, `1` is Solid, `2` is Friendly Fire.
- `coop_player_knockback_strength` [number]<br>
`10` is Weak, `25` is Normal, `60` is Too Much.
These are the values for the default settings, but any number can be used here.
- `coop_stay_in_level_after_star` [0|1|2]<br>
`0` is Leave Level, `1` is Stay In Level, `2` is Nonstop.
- `coop_nametags` [true|false]
- `coop_mod_dev_mode` [true|false]
- `coop_bouncy_bounds` [0|1|2]<br>
`0` is Off, `1` is On, `2` is On (Capped).
- `skip_intro` [true|false]
- `pause_anywhere` [true|false]
- `player_pvp_mode` [0|1]<br>
`0` is Classic, `1` is Revamped.
- `amount_of_players` [number]<br>
Minimum amount is `2`, maximum amount is `16` (for now).
- `bubble_death` [true|false]
### Moderation
You can get a player's coopnet id by using `/players` in the chatbox. Yes you need to type in their entire ID manually. To have multiple moderators or banned players, add a new `moderator:` or `ban:` line. These lines can be removed to remove a player's `moderator:` or `ban:` status.
- `moderator:` [coopnet id]
- `ban:` [coopnet id]
## Coopnet
Annoyingly enough, for a headless server like this, changing the `coopnet_password` field will not set the password of the coopnet server. This instead needs to be done in `compose.yaml`. There is a comment in there to tell you want to change.
