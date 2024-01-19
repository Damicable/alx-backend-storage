-- Indexing first name script
CREATE INDEX idx_name_first ON names(name(1));
