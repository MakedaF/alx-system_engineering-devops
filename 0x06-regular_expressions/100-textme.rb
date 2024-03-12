#!/usr/bin/env ruby
puts ARGV[0].scan((\+\d{11})|(-*[0-9]:-*[0-9]:-*[0-9]:-*[0-9]:-*[0-9])).join
