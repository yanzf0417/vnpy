XTP_LOG_LEVEL = {
    "XTP_LOG_LEVEL_FATAL": "int",
    "XTP_LOG_LEVEL_ERROR": "int",
    "XTP_LOG_LEVEL_WARNING": "int",
    "XTP_LOG_LEVEL_INFO": "int",
    "XTP_LOG_LEVEL_DEBUG": "int",
    "XTP_LOG_LEVEL_TRACE": "int",
}

XTP_PROTOCOL_TYPE = {
    "XTP_PROTOCOL_TCP": "int",
    "XTP_PROTOCOL_UDP": "int",
}

XTP_EXCHANGE_TYPE = {
    "XTP_EXCHANGE_SH": "int",
    "XTP_EXCHANGE_SZ": "int",
    "XTP_EXCHANGE_UNKNOWN": "int",
}

XTP_MARKET_TYPE = {
    "XTP_MKT_INIT": "int",
    "XTP_MKT_SZ_A": "int",
    "XTP_MKT_SH_A": "int",
    "XTP_MKT_UNKNOWN": "int",
}

XTP_PRICE_TYPE = {
    "XTP_PRICE_LIMIT": "int",
    "XTP_PRICE_BEST_OR_CANCEL": "int",
    "XTP_PRICE_BEST5_OR_LIMIT": "int",
    "XTP_PRICE_BEST5_OR_CANCEL": "int",
    "XTP_PRICE_ALL_OR_CANCEL": "int",
    "XTP_PRICE_FORWARD_BEST": "int",
    "XTP_PRICE_REVERSE_BEST_LIMIT": "int",
    "XTP_PRICE_LIMIT_OR_CANCEL": "int",
    "XTP_PRICE_TYPE_UNKNOWN": "int",
}

XTP_ORDER_ACTION_STATUS_TYPE = {
    "XTP_ORDER_ACTION_STATUS_SUBMITTED": "int",
    "XTP_ORDER_ACTION_STATUS_ACCEPTED": "int",
    "XTP_ORDER_ACTION_STATUS_REJECTED": "int",
}

XTP_ORDER_STATUS_TYPE = {
    "XTP_ORDER_STATUS_INIT": "int",
    "XTP_ORDER_STATUS_ALLTRADED": "int",
    "XTP_ORDER_STATUS_PARTTRADEDQUEUEING": "int",
    "XTP_ORDER_STATUS_PARTTRADEDNOTQUEUEING": "int",
    "XTP_ORDER_STATUS_NOTRADEQUEUEING": "int",
    "XTP_ORDER_STATUS_CANCELED": "int",
    "XTP_ORDER_STATUS_REJECTED": "int",
    "XTP_ORDER_STATUS_UNKNOWN": "int",
}

XTP_ORDER_SUBMIT_STATUS_TYPE = {
    "XTP_ORDER_SUBMIT_STATUS_INSERT_SUBMITTED": "int",
    "XTP_ORDER_SUBMIT_STATUS_INSERT_ACCEPTED": "int",
    "XTP_ORDER_SUBMIT_STATUS_INSERT_REJECTED": "int",
    "XTP_ORDER_SUBMIT_STATUS_CANCEL_SUBMITTED": "int",
    "XTP_ORDER_SUBMIT_STATUS_CANCEL_REJECTED": "int",
    "XTP_ORDER_SUBMIT_STATUS_CANCEL_ACCEPTED": "int",
}

XTP_TE_RESUME_TYPE = {
    "XTP_TERT_RESTART": "int",
    "XTP_TERT_RESUME": "int",
    "XTP_TERT_QUICK": "int",
}

ETF_REPLACE_TYPE = {
    "ERT_CASH_FORBIDDEN": "int",
    "ERT_CASH_OPTIONAL": "int",
    "ERT_CASH_MUST": "int",
    "ERT_CASH_RECOMPUTE_INTER_SZ": "int",
    "ERT_CASH_MUST_INTER_SZ": "int",
    "ERT_CASH_RECOMPUTE_INTER_OTHER": "int",
    "ERT_CASH_MUST_INTER_OTHER": "int",
    "EPT_INVALID": "int",
}

XTP_TICKER_TYPE = {
    "XTP_TICKER_TYPE_STOCK": "int",
    "XTP_TICKER_TYPE_INDEX": "int",
    "XTP_TICKER_TYPE_FUND": "int",
    "XTP_TICKER_TYPE_BOND": "int",
    "XTP_TICKER_TYPE_OPTION": "int",
    "XTP_TICKER_TYPE_UNKNOWN": "int",
}

XTP_BUSINESS_TYPE = {
    "XTP_BUSINESS_TYPE_CASH": "int",
    "XTP_BUSINESS_TYPE_IPOS": "int",
    "XTP_BUSINESS_TYPE_REPO": "int",
    "XTP_BUSINESS_TYPE_ETF": "int",
    "XTP_BUSINESS_TYPE_MARGIN": "int",
    "XTP_BUSINESS_TYPE_DESIGNATION": "int",
    "XTP_BUSINESS_TYPE_ALLOTMENT": "int",
    "XTP_BUSINESS_TYPE_STRUCTURED_FUND_PURCHASE_REDEMPTION": "int",
    "XTP_BUSINESS_TYPE_STRUCTURED_FUND_SPLIT_MERGE": "int",
    "XTP_BUSINESS_TYPE_MONEY_FUND": "int",
    "XTP_BUSINESS_TYPE_OPTION": "int",
    "XTP_BUSINESS_TYPE_EXECUTE": "int",
    "XTP_BUSINESS_TYPE_FREEZE": "int",
    "XTP_BUSINESS_TYPE_UNKNOWN": "int",
}

XTP_ACCOUNT_TYPE = {
    "XTP_ACCOUNT_NORMAL": "int",
    "XTP_ACCOUNT_CREDIT": "int",
    "XTP_ACCOUNT_DERIVE": "int",
    "XTP_ACCOUNT_UNKNOWN": "int",
}

XTP_FUND_TRANSFER_TYPE = {
    "XTP_FUND_TRANSFER_OUT": "int",
    "XTP_FUND_TRANSFER_IN": "int",
    "XTP_FUND_INTER_TRANSFER_OUT": "int",
    "XTP_FUND_INTER_TRANSFER_IN": "int",
    "XTP_FUND_TRANSFER_UNKNOWN": "int",
}

XTP_FUND_OPER_STATUS = {
    "XTP_FUND_OPER_PROCESSING": "int",
    "XTP_FUND_OPER_SUCCESS": "int",
    "XTP_FUND_OPER_FAILED": "int",
    "XTP_FUND_OPER_SUBMITTED": "int",
    "XTP_FUND_OPER_UNKNOWN": "int",
}

XTP_SPLIT_MERGE_STATUS = {
    "XTP_SPLIT_MERGE_STATUS_ALLOW": "int",
    "XTP_SPLIT_MERGE_STATUS_ONLY_SPLIT": "int",
    "XTP_SPLIT_MERGE_STATUS_ONLY_MERGE": "int",
    "XTP_SPLIT_MERGE_STATUS_FORBIDDEN": "int",
}

XTP_TBT_TYPE = {
    "XTP_TBT_ENTRUST": "int",
    "XTP_TBT_TRADE": "int",
}

XTP_OPT_CALL_OR_PUT_TYPE = {
    "XTP_OPT_CALL": "int",
    "XTP_OPT_PUT": "int",
}

XTP_OPT_EXERCISE_TYPE_TYPE = {
    "XTP_OPT_EXERCISE_TYPE_EUR": "int",
    "XTP_OPT_EXERCISE_TYPE_AME": "int",
}

XTP_POSITION_DIRECTION_TYPE = {
    "XTP_POSITION_DIRECTION_NET": "int",
    "XTP_POSITION_DIRECTION_LONG": "int",
    "XTP_POSITION_DIRECTION_SHORT": "int",
    "XTP_POSITION_DIRECTION_COVERED": "int",
}

XTP_CRD_CR_STATUS = {
    "XTP_CRD_CR_INIT": "int",
    "XTP_CRD_CR_SUCCESS": "int",
    "XTP_CRD_CR_FAILED": "int",
}

