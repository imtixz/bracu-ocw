interface TagProps {
  name: string;
}

export default function Tag({ name }: TagProps) {
  return (
    <p className="py-1 px-3 bg-slate-100 text-sm rounded-xs cursor-pointer">
      {name}
    </p>
  );
}
