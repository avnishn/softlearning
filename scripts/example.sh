softlearning run_example_local examples.development \
    --algorithm SAC \
    --universe gym \
    --domain push \
    --task v2 \
    --exp-name metaworld-example \
    --checkpoint-frequency=100 \
    --gpus=1 \
    --trial-gpus=1 \
    --server-port 4400