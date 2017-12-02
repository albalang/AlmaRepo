# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: Alma
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.almatube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLScY5TxoXkSS7LhewG9lN0bvDplDOwBUT" 	#Playlist Koleksi Filem P. Ramlee
YOUTUBE_CHANNEL_ID_2 = "PLXRJFkFN7HQFEHgOtfHC1kmk-LxwVHwqL" 	#Playlist MTV Lagu Melayu
YOUTUBE_CHANNEL_ID_3 = "" 	#


# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Koleksi Filem P. Ramlee",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://www.lyrics.my/images/artist/40/original.jpg",
		fanart="https://image.slidesharecdn.com/pramleeslideshow-120925102215-phpapp01/95/p-ramlee-1-728.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MTV Lagu Melayu",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://pbs.twimg.com/profile_images/1769126339/MM27_looknfeel.jpg",
		fanart="http://feat.az/uploads/posts/2014-12/1419360182_muzik.jpg",
        folder=True )

		
run()
