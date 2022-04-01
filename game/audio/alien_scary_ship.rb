
define :tense_bass do |sound|
  tense_bass_line = [36, 38, 39, 43]
  loop do
    tense_bass_line.length().times do |i|
      4.times do
        synth sound, note: tense_bass_line[i]
        sleep 0.125
      end
    end
  end
end

sample :ambi_lunar_land

in_thread do
  tense_bass :blade
end

sleep 4

in_thread do
  main_theme = [[60, 1], [62, 0.125], [63, 0.125], [62, 0.125], [59, 0.125], [62, 0.25], [60, 0.25]]
  loop do
    main_theme.length().times do |i|
      synth :blade, note: main_theme[i][0]
      sleep main_theme[i][1]
    end
  end
end
