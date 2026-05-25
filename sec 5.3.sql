INSERT INTO simulations (
    dataset_id,
    n_simulations,
    mean_loss,
    p95_loss,
    p99_loss
)
VALUES (
    1,
    1000,
    0,
    0,
    0
);
SELECT 
    simulations.id,
    datasets.name,
    datasets.insurance_type,
    simulations.n_simulations,
    simulations.mean_loss,
    simulations.p95_loss,
    simulations.p99_loss
FROM simulations
JOIN datasets
ON simulations.dataset_id = datasets.id;