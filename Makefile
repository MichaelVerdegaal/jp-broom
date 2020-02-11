INPUT_DIR := /somewhere/input
OUTPUT_DIR := /somewhere/output
DELIMITER := ""
NUM_JOBS_PER_MACHINE := 10
TWITTER :=

PYTHON := $(shell which python)
INPUT_FILES := $(wildcard $(INPUT_DIR)/**/*.*)
REL_PATHS := $(patsubst $(INPUT_DIR)/%,%,$(INPUT_FILES))
INPUT_EXT := $(suffix $(word 1, $(INPUT_FILES)))

CAT := cat
ifeq ($(INPUT_EXT),gz)
	CAT := zcat
endif

CLEANED_FILES := $(addprefix $(OUTPUT_DIR)/,$(REL_PATHS))

CLEANING_ARGS =
CLEANING_ARGS += --delimiter $(DELIMITER)
CLEANING_ARGS += --n_jobs $(NUM_JOBS_PER_MACHINE)
ifdef TWITTER
	CLEANING_ARGS += --twitter
endif

.PHONY: all
all: $(CLEANED_FILES)

$(CLEANED_FILES): $(INPUT_DIR)/%: $(OUTPUT_DIR)/%
	mkdir -p $(dir $@)
	$(CAT) $< | $(PYTHON) src/main.py $(CLEANING_ARGS) > $@ || rm $@
