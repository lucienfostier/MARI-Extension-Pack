# ------------------------------------------------------------------------------
# Unproject Layer To Image Manager
# ------------------------------------------------------------------------------
# Will do a Quick Unprojection of the current Layer based on Paint Buffer Dimensions and
# place the result in the Image Manager
# ------------------------------------------------------------------------------
# http://mari.ideascale.com
# ------------------------------------------------------------------------------
# Written by Antoni Kujawa, 2014
# ------------------------------------------------------------------------------
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF HE POSSIBILITY OF SUCH DAMAGE.
# ------------------------------------------------------------------------------



import os
import mari



def unprojLayerPaint():

  mari.history.startMacro('Unproject Layer to Image Manager')
  projectionCamera = mari.actions.get ("/Mari/Canvas/Projection/Create Projector") 
  projectionCamera.trigger()
  mari.projectors.current().setName("CurrentLayer")
  mari.projectors.current().setName("CurrentLayer")
  mari.projectors.current().setUseShader("Current Layer")
  mari.projectors.current().setLightingMode(0)
  mari.projectors.current().setSize (4096, 4096)
  mari.projectors.current().setBitDepth (8)
  unprojDir = os.path.expanduser('~') + "/"
  unprojectFileLoc = "{1}{0}.png".format(mari.projectors.current().name(), unprojDir)
  print unprojectFileLoc
  mari.projectors.current().unprojectToFile(unprojectFileLoc)
  mari.projectors.remove("CurrentLayer")
  mari.images.load(unprojectFileLoc)
  mari.tools.setCurrent("Paint Through")
  mari.history.stopMacro()
  return 

def unproject_layer_to_imageman():

  unprojLayerPaint()
