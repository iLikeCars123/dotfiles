# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from libqtile import extension
mod = "mod4"
terminal = guess_terminal()



g1 = "#4b5263"
g2 = "#5c6370"
b2 = "#1e222a"
black = "#282c34"
green = "#98c379"
blue = "#61afef"
white = "#f7f7f7"

max_bright = int(subprocess.getoutput("brightnessctl m"))
def volcontroll(name, way):
    if way == 1:#raise
        qtile.cmd_spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")
    elif way == 2: #lower
        qtile.cmd_spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")
    else:#mute
        qtile.cmd_spawn("pactl set-sink-volume @DEFAULT_SINK@ 0%")

    #volume.cmd_update(subprocess.getoutput("pactl list sinks | grep Volume: | awk \'NR==1{print $5}\'"))
    #volume.cmd_update(subprocess.getoutput("pamixer --get-volume")+"%")
    volume.cmd_update(subprocess.getoutput("pactl list sinks | grep \'^[[:space:]]Volume:\' |     head -n $(( $SINK + 1 )) | tail -n 1 | sed -e \'s,.* \\([0-9][0-9]*\\)%.*,\\1,\'")+"%")

def brightnessctrl(name, way):
    if way == 1:
        qtile.cmd_spawn("brightnessctl s +5%")
    else:
        qtile.cmd_spawn("brightnessctl s 5%-")

    brightness.cmd_update(str(int(subprocess.getoutput("brightnessctl g"))/max_bright))
def switch_screens(x):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

def open_pavu():
    qtile.cmd_spawn("pavucontrol")
def open_wifi():
    qtile.cmd_spawn("rofi-wifi-menu")
def open_power():
    qtile.cmd_spawn("gnome-power-statistics")
def restart_pulse():
    qtile.cmd_spawn("pulseaudio -k")

    
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),


    #Key([mod, "shift"], "z", lazy.window.togroup("3"), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    #Key([mod, "shift"], "f", lazy.window.toggle_max(), desc="toggle fullscreen"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "f", lazy.spawn("firefox"), desc="firefox"),
    Key([mod], "q", lazy.spawn("qutebrowser"), desc="qutebrowser"),
    Key([mod, "shift"], "f", lazy.spawn("firefox -private-window"), desc="firefox private window"),
    Key([mod], "x", lazy.spawn("lite-xl"), desc="lite xl"),
    Key([mod], "n", lazy.spawn("alacritty -e nnn"), desc="file manager"),
    Key([mod], "y", lazy.spawn("libreoffice"), desc="libreoffice"),
    Key([mod], "b", lazy.spawn("alacritty -e bc"), desc="calculator"),
    Key([mod], "e", lazy.spawn("alacritty -e cmus"), desc="music player"),
    Key([mod, "shift"], "r", lazy.spawn("rofimoji"), desc="music player"),
    Key([mod, "shift"], "b", lazy.spawn("rofi -show calc"), desc="music player"),

    Key([mod], "F8", lazy.function(volcontroll, 1), desc="Volume +5%"),
    Key([mod], "F7", lazy.function(volcontroll, 2), desc="Volume -5%"),
    Key([mod], "F6", lazy.function(volcontroll, 3), desc="Mute"),
    Key([mod], "F3", lazy.function(brightnessctrl, 1), desc="brightness +5%"),
    Key([mod], "F2", lazy.function(brightnessctrl, 2), desc="brightness -5%"),
    Key([mod], "s", lazy.to_screen(0), desc='Keyboard focus to monitor 1'),
    Key([mod], "a", lazy.to_screen(1), desc='Keyboard focus to monitor 2'),
         ### Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc='rofi drun'),
    Key([mod], "p", lazy.spawn("/home/david/.config/rofi/applets/menu/powermenu.sh"), desc='rofi drun'),

    Key([mod], "F10", lazy.spawn("playerctl play-pause"), desc='play/pause audio'),
  
    Key([mod], "t", lazy.function(switch_screens), desc="Switch screens workspace"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
#        Key([mod, "shift", "ctrl"], i.name, lazy.window.togroup(i.name),
#             desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(border_focus_stack=green, border_focus=blue, border_normal=white, border_width=3, margin=3),
    layout.Max(),

    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
    #layout.MonadTall(),
    #layout.MonadWide(),
    #layout.RatioTile(),
    layout.Tile(),
    #layout.TreeTab(border_width=3, active_bg=blue),
    #layout.VerticalTile(border_focus_stack='#d75f5f', border_focus=blue, border_width=3, margin=3),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font="Ubuntu Mono Bold",
    fontsize=14,
    padding=4,
    foreground=white
)
extension_defaults = widget_defaults.copy()

volume = widget.TextBox(text=subprocess.getoutput("pactl list sinks | grep \'^[[:space:]]Volume:\' |     head -n $(( $SINK + 1 )) | tail -n 1 | sed -e \'s,.* \\([0-9][0-9]*\\)%.*,\\1,\'")+"%", foreground=blue, background=black, mouse_callbacks={"Button1": open_pavu, "Button3": restart_pulse})

#volume = widget.PulseVolume(foregound=black, background=green, mouse_callbacks={"Button1": open_pavu, "Button3": restart_pulse}
#        , update_interval=.1)

brightness = widget.TextBox(text=str(int(subprocess.getoutput("brightnessctl g"))/max_bright), background=black, foreground=blue)
def copy_bar():
    return bar.Bar(
                [
                widget.Spacer(5),
                widget.TextBox(
                    text="\ue0be",
                    font="Ubuntu Mono Bold",
                    fontsize="41",
                    padding=0,
                    background=black,
                    foreground=blue,
                ),


                widget.GroupBox(padding_y=5, padding_x=5,font = "Source Code Pro Bold", rounded=False,
                highlight_method = "line", borderwidth=4, 
                active=white, inactive=black, highlight_color=g1,
                this_screen_border=black, this_current_screen_border=g1, background=blue),

                widget.TextBox(
                    text="\ue0be",
                    fontsize="41",
                    padding=0,
                    background=blue,
                    foreground=black,
                ),

                #widget.Prompt(),
                widget.Spacer(),
                widget.Systray(icon_size=15, padding=10),
                widget.Spacer(5),
                widget.TextBox(
                    text="\ue0be",
                    fontsize="41",
                    padding=0,
                    background=black,
                    foreground=blue,
                ),

                widget.CurrentLayout(background=blue, foreground=black),

                widget.TextBox(
                    text="\ue0be",
                    fontsize="41",
                    padding=0,
                    background=blue,
                    foreground=black,
                ),
                widget.TextBox(text="🔆", background=black), 
                brightness,                
                widget.TextBox(
                    text="\ue0be",
                    fontsize="41",
                    padding=0,
                    background=black,
                    foreground=blue,
                ),

                widget.Battery(format='🔋{char}{percent:2.0%}', background=blue, foreground=black, mouse_callbacks={"Button1": open_power},),
                widget.TextBox(
                    text="\ue0be",
                    fontsize="41",
                    padding=0,
                    background=blue,
                    foreground=black,
                ),
                widget.TextBox(text="🔈", background=black),
                volume,
                widget.TextBox(
                    text="\ue0be",
                    fontsize="41",
                    padding=0,
                    background=black,
                    foreground=blue,
                ),

                widget.TextBox(text="📶", background=blue),
                widget.Wlan(interface="wlp1s0", foreground=black, background=blue, mouse_callbacks={"Button1": open_wifi},),
                widget.TextBox(
                    text="\ue0be",
                    fontsize="41",
                    padding=0,
                    background=blue,
                    foreground=black,
                ),


                widget.Clock(format='%m-%d-%Y %a %I:%M:%S %p', padding=10, foreground=blue, background=black),
                widget.TextBox(
                    text="\ue0be",
                    fontsize="41",
                    padding=0,
                    background=black,
                    foreground=blue,
                ),

                widget.QuickExit(default_text = "Logout", foreground=black, background=blue),
                widget.Spacer(10, background=blue),
                ],
                24,
                background=black,
                opacity=1,
    )


screens = [

    Screen(
        wallpaper="~/Pictures/crane.png",
        wallpaper_mode="fill",
        top=copy_bar()
        ),
    
]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]



dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def autostart():
#    home = os.path.expanduser('~')
#    subprocess.call([home + '/.config/qtile/autostart.sh'])
    os.system('picom &')
#    os.system('udiskie &')

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
