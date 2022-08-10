#!/usr/bin/env ruby
val = ARGV[0]

if val == nil
  return
end
print val.scan(/\w[t.]{2,5}/)
