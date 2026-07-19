CC ?= cc
CFLAGS ?= -O2 -Wall -Wextra -Wpedantic -std=c11
LDFLAGS ?=
TARGET := baseline-config-demo
SRC := src/baseline_config_demo.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -D_DEFAULT_SOURCE $< -o $@ $(LDFLAGS)

clean:
	rm -f $(TARGET)
