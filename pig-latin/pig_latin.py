def translate(words):
  pig = []
  for word in words.split(' '):
    if word[0] in ('a', 'e', 'i', 'o', 'u'):
      pig.append(word + 'ay')
    elif word[:2] in ('yt', 'xr'):
      pig.append(word + 'ay')
    elif word[:3] in ('sch', 'squ', 'thr'):
      pig.append(word[3:] + word[:3] + 'ay')
    elif word[:2] in ('ch', 'qu', 'th'):
      pig.append(word[2:] + word[:2] + 'ay')
    else:
      pig.append(word[1:] + word[:1] + 'ay')

  return ' '.join(pig)
