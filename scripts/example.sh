softlearning run_example_local examples.development \
    --algorithm SAC
    --universe gym \
    --domain push-v1 \
    --task v1 \
    --exp-name metaworld-example \
    --checkpoint-frequency=5 \
    --gpus=1 \
    --trial-gpus=1