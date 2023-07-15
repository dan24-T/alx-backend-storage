-- Creates ind  using thee first letter

CREATE INDEX idx_name_first_score ON names (name(1), score);
