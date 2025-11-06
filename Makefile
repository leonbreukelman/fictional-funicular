.PHONY: setup-aws check-prerequisites create-feature

setup-aws:
	@./.specify/scripts/bash/check-prerequisites.sh
	@./.specify/scripts/bash/setup-plan.sh
	@echo "AWS setup complete. Default region: us-east-1."

check-prerequisites:
	@./.specify/scripts/bash/check-prerequisites.sh

create-feature:
	@./.specify/scripts/bash/create-new-feature.sh
