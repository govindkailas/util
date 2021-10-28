# # -*- coding: utf-8 -*-
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#  fstab yaml to fstab entry file
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import yaml
import sys
with open(sys.argv[1], 'r') as f:
    try:
        doc = yaml.load(f, Loader=yaml.FullLoader)
        lines = []

        for k, v in doc.items():
            if type(v) is dict:
                for k1, v1 in v.items():
                    #fstab output format, we will treat the below line as a template and feed details to it
                    _mount, _type, _export, _options, _reserve, _defaults = '', '', '', '', '', 'defaults'
                    _main = k1
                    if 'mount' in v1:
                        _mount = v1['mount']
                    if 'type' in v1:
                        _type = v1['type']
                    if 'export' in v1:
                        _export = v1['export']
                    if 'root-reserve' in v1:
                        _reserve = v1['root-reserve']
                    if 'options' in v1:
                        _options = ','.join(v1['options'])
                        _defaults = ''

                    line = f'{_main} {_mount} {_export} {_type} {_reserve} {_options} {_defaults} 0 0'
                    lines.append(line)

        with open('fstab-output.txt', 'w') as _obj:
            _obj.writelines('\n'.join(lines))
        print('Output file for fstab generated!, check out fstab-output.txt')    
    except yaml.YAMLError as exc:
        print(exc)