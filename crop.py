from pydub import AudioSegment

f_name = 'elven ranger'
f_type = 'm4a'
path = f'{f_name}.{f_type}'
track = AudioSegment.from_file(f'{f_name}.{f_type}', format=f_type)

track[180*1000:600*1000].export(f'{f_name}_out.{f_type}', format=f_type)

