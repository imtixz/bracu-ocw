import { useNavigate } from "react-router";
import Tag from "./Tag";

interface CourseCardProps {
  code: string;
  title: string;
  level: "UNDERGRADUATE" | "GRADUATE";
  description: string;
  tags: string[];
}

export default function CourseCard({
  code,
  title,
  level,
  description,
  tags,
}: CourseCardProps) {
  const navigate = useNavigate();

  return (
    <div
      className="bg-white flex flex-col mx-2 sm:mx-8 px-5 py-6 rounded shadow-md/30"
      onClick={() => {
        navigate(`/details?course=${code.toLowerCase()}`);
      }}
    >
      <p className="text-sm font-bold text-emerald-600">
        {code} | {level}
      </p>
      <p className="text-lg font-bold hover:underline cursor-pointer">
        {title}
      </p>
      <p>{description}</p>
      <div className="flex flex-row gap-x-3 mt-3 flex-wrap">
        {tags.map((t, i) => (
          <div key={i} className="my-1">
            <Tag name={t} />
          </div>
        ))}
      </div>
    </div>
  );
}
