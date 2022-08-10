#!/usr/bin/env ruby
val = ARGV[0]

if val == nil
  return
end
print val.scan(/School/).join("")

