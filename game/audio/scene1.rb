# Welcome to Sonic Pi

sample :ambi_swoosh, amp: 4
sleep 1.5

notes = [[60, 0.5], [72, 1]]

notes.length().times do |i|
  synth :pulse, note: notes[i][0], attack: 0.2, sustain: 0.4
  sleep notes[i][1]
end

define :pattern do |sound, notes, durations|
  notes.length().times do |i|
    synth sound, note: notes[i]
    sleep durations[i]
  end
end

in_thread do
  6.times do |tick|
    if tick == 3
      cue :level2
    end
    
    motive1 = [0.25, 0.25, 0.125, 0.125, 0.75]
    notes1 = [60, 60, 59, 60]
    notes2 = [65, 64, 62, 64]
    
    notes2.length().times do |i|
      pattern :blade, notes1 + [notes2[i]], motive1
    end
  end
end

sync :level2
motive2 = [0.875, 0.125, 0.25, 0.25]
3.times do
  notes3 = [[72, 71, 69, 67], [71, 69, 67, 65], [69, 67, 65, 64], [65, 64, 62, 60]]
  notes3.length().times do |i|
    pattern :chiplead, notes3[i], motive2
  end
end


synth :blade, note: [60, 64, 67], attack: 0.5, sustain: 1

