def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    inter_recom_relevant = set (recommended[:k]).intersection(set(relevant))

    precision_k = len(inter_recom_relevant)/k
    recall_k = len(inter_recom_relevant)/len(relevant)

    return [precision_k, recall_k]

    