-- Creates index using our first letter

CREATE INDEX idx_name_first 
  ON names (name(1));
