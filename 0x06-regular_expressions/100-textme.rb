#!/usr/bin/env ruby
  log_line = ARGV[0]
  
  regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

  match_data = log_line.match(regex)

  if match_data
    sender = match_data[1]
    receiver = match_data[2]
    flags = match_data[3]
  
    sender.strip!
    receiver.strip!
    flags.strip!

    puts "#{sender},#{receiver},#{flags}"
  end
  