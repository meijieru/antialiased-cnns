# Copyright (c) 2019, Adobe Inc. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
# 4.0 International Public License. To view a copy of this license, visit
# https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.

import antialiased_cnns

filter_size = 4 # can be 2,3,4,5
pretrained = True

model = antialiased_cnns.resnet.resnet18(pretrained=pretrained, filter_size=filter_size)
model = antialiased_cnns.resnet.resnet34(pretrained=pretrained, filter_size=filter_size)
model = antialiased_cnns.resnet.resnet50(pretrained=pretrained, filter_size=filter_size)
model = antialiased_cnns.resnet.resnet101(pretrained=pretrained, filter_size=filter_size)

model = antialiased_cnns.alexnet.alexnet(pretrained=pretrained, filter_size=filter_size)

model = antialiased_cnns.vgg.vgg16(pretrained=pretrained, filter_size=filter_size)
model = antialiased_cnns.vgg.vgg16_bn(pretrained=pretrained, filter_size=filter_size)

model = antialiased_cnns.densenet.densenet121(pretrained=pretrained, filter_size=filter_size)

model = antialiased_cnns.mobilenet.mobilenet_v2(pretrained=pretrained, filter_size=filter_size)

