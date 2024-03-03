-- 코드를 입력하세요
-- SELECT flavor from july group by flavor;
-- SELECT 
--    J.FLAVOR,
--    (SUM(J.TOTAL_ORDER) + SUM(F.TOTAL_ORDER)) AS TOTAL_ORDER
    
-- FROM FIRST_HALF AS F
-- JOIN JULY AS J
-- ON F.FLAVOR = J.FLAVOR

-- GROUP BY F.FLAVOR
-- ORDER BY TOTAL_ORDER DESC
-- LIMIT 3;

select flavor
from first_half a
join july b using (flavor)
group by flavor
order by sum(a.total_order + b.total_order) desc
limit 3;
