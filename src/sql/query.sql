WITH total AS
(
	SELECT  match_id,championname as champion_lose
	       ,COUNT(*) AS lose
	FROM league
	WHERE role = 'JUNGLE'
	AND win = true
	and date(game_start) >= '2/9/2023'
	GROUP BY  1,2
	ORDER BY 2 desc),
	 wins AS
(
	SELECT  match_id,championname as champion_win
	       ,COUNT(*) AS wins
	FROM league
	WHERE role = 'JUNGLE'
	AND win = false
	and date(game_start) >= '2/9/2023'
	GROUP BY  1,2
	ORDER BY 2 desc
),matchup as (
select *
from total t 
join wins w 
on t.match_id = w.match_id)
select champion_win, champion_lose,count(*)
from matchup
group by 1,2
order by 3 desc
limit 10