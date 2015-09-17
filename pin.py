def ComputeChecksum(PIN):
   accum = 0;
   PIN *= 10;
   accum += 3 * ((PIN / 10000000) % 10);
   accum += 1 * ((PIN / 1000000) % 10);
   accum += 3 * ((PIN / 100000) % 10);
   accum += 1 * ((PIN / 10000) % 10);
   accum += 3 * ((PIN / 1000) % 10);
   accum += 1 * ((PIN / 100) % 10);
   accum += 3 * ((PIN / 10) % 10);
   digit = (accum % 10);
   return (10 - digit) % 10;
print ComputeChecksum(num)
